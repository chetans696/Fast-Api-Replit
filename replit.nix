{pkgs}: {
  deps = [
    pkgs.glibcLocales
    pkgs.python311Packages.uvicorn
  ];
}
