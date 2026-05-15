class GitProvider:
    def list_files(self, source): raise NotImplementedError
    def fetch_file(self, source, path): raise NotImplementedError
    def export_to_temp(self, source): raise NotImplementedError
