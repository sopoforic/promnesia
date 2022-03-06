class Site:
    def supports(url):
        raise NotImplementedError

    def canonify(url):
        from promnesia.cannon import canonify
        return canonify(url)
