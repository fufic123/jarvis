# Jarvis Roadmap

### MVP 0 (CLI) Basic funcs

#### v0.1.0
`/echo` - no params, returning `200`  
`/yo` - no params, returning `Hello World`  
`/joke` - no params, returning `he-he-he`

#### v0.1.1
debug (DebugMixin)

#### v0.1.2
beautify logging (ColorFormatter)

#### v0.1.3
plugins map instead of loop

#### v0.2.0
`/echo params` - returning params  
`/yo`, `/hi`, `/hello` - same command, returning `Hello World`  
`/joke` - returning `he-he-he`  
`/help` - list of all commands

#### v0.2.1
`/help cmd` - explanation of the command  
Suggest similar commands:  
Example `/echw`, `.echw`, `/wcho` → `Maybe you mean /echo`

#### v0.2.2
switch to async/await (run async plugins)

#### v0.2.3
`/memory`
subcommands support:  
`/memory set key value`, `/todo add task`, etc.

#### v0.3.0
✅ `/todo` — add/list/delete  
✅ `/notify` — send console or system alerts  
✅ `/time` — show current time (user timezone)

#### v0.3.1
🧠 Basic memory system used **only inside plugins** (e.g., `/notify`)  
Not available to user directly yet

#### v0.3.2
🤖 Agent system base  
- Passive agents: react to triggers (time-based or context-based)  
- `/agent list`  
- Background tick loop

#### v0.3.3
Natural Language → command mapping (NLP router)  
- `/do remind me to drink water in 5 minutes`  
→ calls `/todo add "drink water"` or `/notify`  
Powered by simple rules or spaCy/NLTK