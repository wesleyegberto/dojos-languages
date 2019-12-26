# IO and File System

# === IO Module ===
# Main mechanism for reading and writing to standard input/output (`:stdio`), error (`:stderr`),
# files and others devices.

IO.puts("Hello world!")
IO.puts(['Hello', ' ', 'World'])
IO.gets("Enter a message: ")

IO.puts(:stderr, "Hello world of stderr")


# === File Module ===
# File module contains functions that allow to open files as IO devices.
# By default, files are opened in binary mode and requires devs to use `IO.binread/2` and `IO.binwrite/2`.
# But we can also open using `:utf8` encoding.
# The functions in File module are named after their UNIX equivalents: `File.rm/1`, `File.mkdir/1`, `File.mkdir_p/1`, `File.cp_r/2`, `File.rm_rf/1`.

{:ok, file} = File.open("hello_file.txt", [:write])
IO.binwrite(file, "Message to be written")
File.close(file)

# read returns a tuple with the result status (:ok or :error) and its content
{:ok, fileContent} = File.read("hello_file.txt")
# we can use trailing bang (!) to received the content (but it will raise error if anything goes wrong)
fileContent = File.read("hello_file.txt")

# read an inexisting file without raise an error
{ :error, :enoent } = File.read("this_file_does_not_exist.none") # the match asserts that it returns an error
# read and raise an error
File.read!("this_file_does_not_exist.none")


# we can use the version without ! to handle different outcomes
case File.read("hello_file.txt") do
    {:ok, content} -> IO.puts content
    {:error, reason} -> IO.puts "Error: #{reason}"
end

# when we expect the file to be there is more useful to use the bang variation because the matching
# will failt and obscure the actual error.
{:ok, body } = File.read("some_weird_file") # the error raised will be about the match fail instead of file not existing

body = File.read!("some_weird_file") # now we will see that the file does not exist


# === Path module ===
# File module expect paths as arguments (which are specific by OS).
# Path module provides functions to working with paths in a generic way (OS-agnostic).

# returns foo/bar on unix-like and foo\bar on windows
Path.join("foo", "bar")

# returns complete path (/Users/username/hello or C:\Users\username\hello)
Path.expand("~/hello")



# === File as Process ===
# The IO module actually works with processes. Given a file is a process, when we write to a file
# we are actually sending a message with the content to write. When this file is closed the process is terminated.
# By modeling IO devices with processes, Earlang VM allows IO messages to be routed between different
# nodes running Distributed Erlang or even exchange files to perform read/write operations across nodes.

{:ok, file} = File.open("hello.txt", [:write])
File.close(file)
# we closed the file, thus the processed is terminated
{:error, :terminated} = IO.write(file, "Is anybody out there")


# mocking a file
pid = spawn fn ->
    receive do: (msg -> IO.inspect msg)
end

IO.write(pid, "hello mocked file")

