# nvim-file-recv
Hacky script to "send a file to (n)vim"

## Installation
0. install flask v2.x globally
1. git clone this to `$HOME`
2. add the following line to `.vimrc`:
```vimrc
:command FileRecv execute '!$HOME/nvim-FileRecv/run.sh "%"' | r!tail -1 /tmp/nvim-file-recv
```

## Behaviour
When you type `:FileRecv` in vim,
1. a very simple file upload website (Flask server) will begin running on `0.0.0.0:8000`
2. once a file is manually uploaded on that site, the server will shutdown
3. the uploaded file will be saved to the directory containing the current open file, and the path to that file will be dumped in the current buffer

## QnA
#### Couldn't you use `magic-wormhole` / `scp` / an actual file server?
I have extensively used all of the aforementioned solutions. This solution is more ergonomic/efficient, even if hacky.

#### Why not make a vim plugin?
I don't know how to host a HTTP server in that.

#### Isn't this insecure?
Highly so.

#### It doesn't work!
works on my machine

### Have you seen `<project>`? It does what this repo does but way cooler
I have not; please send it my way!
