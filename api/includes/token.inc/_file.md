# includes/token.inc

- **Source:** [local](../../../source/includes/token.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/token.inc) · 265 lines

## File documentation

```text
@file
Drupal placeholder/token replacement system.

API functions for replacing placeholders in text with meaningful values.

For example: When configuring automated emails, an administrator enters
standard text for the email. Variables like the title of a node and the date
the email was sent can be entered as placeholders like [node:title] and
[date:short]. When a Drupal module prepares to send the email, it can call
the token_replace() function, passing in the text. The token system will
scan the text for placeholder tokens, give other modules an opportunity to
replace them with meaningful text, then return the final product to the
original module.

Tokens follow the form: [$type:$name], where $type is a general class of
tokens like 'node', 'user', or 'comment' and $name is the name of a given
placeholder. For example, [node:title] or [node:created:since].

In addition to raw text containing placeholders, modules may pass in an array
of objects to be used when performing the replacement. The objects should be
keyed by the token type they correspond to. For example:

@code
// Load a node and a user, then replace tokens in the text.
$text = 'On [date:short], [user:name] read [node:title].';
$node = node_load(1);
$user = user_load(1);

// [date:...] tokens use the current date automatically.
$data = array('node' => $node, 'user' => $user);
return token_replace($text, $data);
@endcode

Some tokens may be chained in the form of [$type:$pointer:$name], where $type
is a normal token type, $pointer is a reference to another token type, and
$name is the name of a given placeholder. For example, [node:author:mail]. In
that example, 'author' is a pointer to the 'user' account that created the
node, and 'mail' is a placeholder available for any 'user'.

@see token_replace()
@see hook_tokens()
@see hook_token_info()
```

## Functions (derived index)

- [token_replace()](token_replace.md) — Replaces all tokens in a given string with appropriate values.
- [token_scan()](token_scan.md) — Builds a list of all token-like patterns that appear in the text.
- [token_generate()](token_generate.md) — Generates replacement values for a list of tokens.
- [token_find_with_prefix()](token_find_with_prefix.md) — Returns a list of tokens that begin with a specific prefix.
- [token_info()](token_info.md) — Returns metadata describing supported tokens.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
