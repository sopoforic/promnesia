class Site:
    def supports(url):
        raise NotImplementedError

    def canonify(url):
        from promnesia.cannon import old_canonify
        return old_canonify(url)
