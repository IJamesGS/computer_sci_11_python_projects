{
  pkgs,
  lib,
  config,
  inputs,
  ...
}:

{
  packages = with pkgs; [
    git
    rumdl
    ruff
    ty
  ];

  languages.python = {
    enable = true;
    package = pkgs.python314;
    lsp.enable = false; # Only supports `pyright`; doesn't fit requirements
    venv.enable = true;
    venv.requirements = ''
      pytest==9.0.3
    '';
  };

  enterTest = ''
    echo "Running tests"
    git --version | grep --color=auto "git version ${pkgs.git.version}"
    rumdl --version | grep --color=auto "rumdl ${pkgs.rumdl.version}"
    ruff --version | grep --color=auto "ruff ${pkgs.ruff.version}"
    ty --version | grep --color=auto "ty ${pkgs.ty.version}"
  '';

  # See full Devenv reference at https://devenv.sh/reference/options/
}
