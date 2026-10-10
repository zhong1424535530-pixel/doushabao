import re


class ConversationMemory:
    def __init__(self, max_messages=12, max_threads=300):
        self.max_messages = max_messages
        self.max_threads = max_threads
        self._by_bot_message_id = {}

    def remember(self, bot_message_id, messages):
        trimmed = self._trim(messages)
        self._by_bot_message_id[int(bot_message_id)] = trimmed

        if len(self._by_bot_message_id) > self.max_threads:
            oldest_id = next(iter(self._by_bot_message_id))
            del self._by_bot_message_id[oldest_id]

    def has_thread(self, bot_message_id):
        return int(bot_message_id) in self._by_bot_message_id

    def messages_for_reply(self, replied_bot_message_id, user_content):
        previous = self._by_bot_message_id.get(int(replied_bot_message_id), [])
        return self._trim([*previous, {"role": "user", "content": user_content}])

    def messages_for_new_question(self, user_content):
        return [{"role": "user", "content": user_content}]

    def _trim(self, messages):
        return list(messages[-self.max_messages :])


def build_grok_tools():
    return [{"type": "web_search"}, {"type": "x_search"}]


def build_grok_user_content(user_text, image_data_urls=None):
    image_data_urls = image_data_urls or []
    if not image_data_urls:
        return user_text

    return [
        {"type": "text", "text": user_text},
        *[
            {"type": "image_url", "image_url": {"url": image_data_url}}
            for image_data_url in image_data_urls
        ],
    ]


async def with_optional_typing(typing_context, action):
    try:
        await typing_context.__aenter__()
    except Exception:
        return await action()

    try:
        return await action()
    finally:
        await typing_context.__aexit__(None, None, None)


def split_discord_message(text, limit=2000):
    if len(text) <= limit:
        return [text]

    chunks = []
    remaining = text
    while remaining:
        chunks.append(remaining[:limit])
        remaining = remaining[limit:]
    return chunks


def strip_think_blocks(text):
    return re.sub(r"<think>.*?</think>\s*", "", text, flags=re.DOTALL).strip()
