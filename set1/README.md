# Writeup for Set 1 Challenges

## Challenge 1

This challenge is a good excuse to get a clear understanding of a few interrelated topics.
- How `text` is represented in `binary`
- The `Base64` encoding system

### _Text_ representation in _`Binary`_

There's a [video](https://www.youtube.com/watch?v=MijmeoH9LT4&t=6s) on the [Computerphile](https://www.youtube.com/user/Computerphile/) channel in YouTube, (which I'm a big fan of) which explains this topic very simply and precisely. You can find that video [here](https://www.youtube.com/watch?v=MijmeoH9LT4&t=6s).

`TODO: Add a basic explanation of the topic`

### _`Base64`_ Encoding

`Base64` is an way of converting binary data (you can think of it as a long string of 0s and 1s) into printable `ASCII` text. This is a way of sending arbitrary data (eg. images, executables, music, etc.) over channels which only support text. This is used most prominently in e-mail attachments. When the receiver receives the `Base64` encrypted data, they can convert it back to its original form.
