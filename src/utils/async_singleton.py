import asyncio


class AsyncSingleton:
    _instance = None
    _lock = asyncio.Lock()

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            # インスタンスだけはここで作る（非同期できない）
            cls._instance = super().__new__(cls)
        return cls._instance

    @classmethod
    async def get_instance(cls, *args, **kwargs):
        if cls._instance is None:
            async with cls._lock:
                if cls._instance is None:
                    instance = cls()
                    # 初期化後に代入する（ここが重要！）
                    if hasattr(instance, "_async_initialize"):
                        await instance._async_initialize(*args, **kwargs)
                    elif hasattr(instance, "_initialize"):
                        instance._initialize(*args, **kwargs)
                    cls._instance = instance
        return cls._instance

    # async def _async_initialize(self, *args, **kwargs):
    #     pass

    # def _initialize(self, *args, **kwargs):
    #     pass
