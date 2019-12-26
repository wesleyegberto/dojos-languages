# Processes
# In Elixir, all code runs inside processes and are extremely lightweight in terms of memory and CPU.
# Processes are isolated from each other, run concurrent to one another and communicate via messaging passing.
# Used to build concurrency, distributed and fault-tolerant programs.

# === spawn ===
# Basic mechanism for spawning new process

pid = spawn fn -> 1 + 2 end
Process.alive?(pid)

own_pid = self()
Process.alive?(own_pid)


# === send ===
# We use `send` function to emit a message to another process. The messages sent are stored in
# the process mailbox.
send self(), { :hello, "world" }

# === receive ===
# We use `receive` function to handle mailbox of messages of current process. The `receive` supports
# guards and many clauses like `case/2`.
receive do
    { :hello, message } -> "Received: #{message}"
    { _, message } -> "Won't match: #{message}"
end

# If there is no message in the mailbox matching any of the patterns, the current process will
# wait until a matching message arrives.
# A timeout can also be specified. 0 can be given when we already expect the message to be in the mailbox.
receive do
    { :hello, message } -> "Received: #{message}"
    after 1_000 -> "Nothing after 1s"
end

# `flush/0` is useful to print all the messages in the mailbox and flushes it (consume).
flush()

# We can use `inspect/1` to convert a data structure's internal representation into a string.
inspect self()


# Example to create a process to just send a message to the parent
parent = self()
spawn fn -> send(parent, { :hello, self() }) end

receive do
    { :hello, pid } -> "Got hello from process #{inspect pid}"
end


# We can use `Process.register/2` to register a process and give it a name
Process.register(self(), :MAIN_PROCESS)
spawn fn -> send(:MAIN_PROCESS, { :hello, "#{inspect self()} - message to MAIN_PROCESS" }) end

receive do
    { :hello, pid } -> "Received: #{inspect pid}"
end


# === Links ===

# When using `spawn` the created processed is not linked, so when it raises an error the parent won't even know.
spawn fn -> raise "A unnoted error" end

# We can use `spawn_link/1` to created a linked process, if it raises an error the parent will know.
spawn_link fn -> raise "A noted error" end

# We can link a process manually with `Process.link/1`.


# === Tasks ===
# A abstraction built on top of `spawn/1` and `spawn_link/1` to provide a better error reports and instrospection.
# The module provides `Task.start/1` and `Task.start_link/1` which return `{ :ok, pid }`.
# This is what enables tasks to be used in supervision trees.
# Task also provides convenience functions like `Task.async/1` and `Task.await/1`.
Task.start fn -> raise "Error that will be reported" end
Task.start_link fn -> raise "Error that will be reported and noted" end



# === State ===
# Processes are the most common way to keep state (application cofniguration, parsed files, so on).
# Although we are not going to do this manually (we will use abstraction like Agents).

# Example of use: process with Key-Value store

# module to created a process as Key-Value store
defmodule KeyValueStore do
    def start_link do
        # create a process keeping a loop
        Task.start_link(fn -> loop(%{}) end)
    end

    defp loop(map) do
        # blocks until someone sent it an action (:get or :put)
        receive do
            { :get, key, callerPid } ->
                # send the requested key value
                send callerPid, Map.get(map, key)
                loop(map)
            { :put, key, value } ->
                loop(Map.put(map, key, value))
        end
    end
end

{ :ok, kvStorePid } = KeyValueStore.start_link
# register to facilitate the use
Process.register(kvStorePid, :KEY_VALUE_STORE)

# send a message requesting the value
send :KEY_VALUE_STORE, { :get, :hello, self() }
flush() # will print a nil

# puts a key and value
send :KEY_VALUE_STORE, { :put, :hello, "world" }
flush() # will print "world"


# Same example using agents
{ :ok, kvStorePid } = Agent.start_link(fn -> %{} end)
# puts a key-value into the map
Agent.update(kvStorePid, fn map -> Map.put(map, :hello, :world) end)
Agent.get(kvStorePid, fn map -> Map.get(map, :hello) end)
