tag: terminal
and tag: user.cargo
-
cargo format: "cargo fmt\n"
cargo build: "cargo build\n"
cargo build release: "cargo build --release\n"
cargo check: "cargo check\n"
cargo check all features: insert("cargo check --all-features\n")
cargo test [<user.format_text>]:
    insert("cargo test")
    insert(format_text or "")
    insert("\n")
cargo clean: "cargo clean\n"
cargo bench: "cargo bench\n"
cargo add [<user.format_text>]:
    insert("cargo add ")
    insert(format_text or "")
cargo fix: "cargo fix"
cargo tree: "cargo tree"
