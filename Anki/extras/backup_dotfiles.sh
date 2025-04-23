#!/bin/bash

DEST=~/dotfiles_backup

# Create folders if they don't exist
mkdir -p $DEST/.config $DEST/.ssh

# Tmux
#cp ~/.tmux.conf $DEST/

# Zsh
cp ~/.zshrc $DEST/
cp -r ~/.oh-my-zsh $DEST/ 2>/dev/null

# Neovim
cp -r ~/.config/nvim $DEST/.config/

# Alacritty
cp -r ~/.config/alacritty $DEST/.config/

# Git
cp ~/.gitconfig $DEST/

# SSH Keys (⚠️ Secure these if syncing to cloud)
cp -r ~/.ssh $DEST/

# Optional: List other configs you want to include
