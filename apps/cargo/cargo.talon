tag: terminal
and tag: user.cargo
-
cargo format: insert("cargo fmt\n")
cargo build: insert("cargo build\n")
cargo build release: insert("cargo build --release\n")
cargo check: insert("cargo check\n")
cargo check all features: insert("cargo check --all-features\n")
cargo test [<user.format_text>]:
    insert("cargo test")
    insert(format_text or "")
    insert("\n")
