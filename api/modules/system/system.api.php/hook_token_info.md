# hook_token_info()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 4565–4602 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L4565-L4602)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_token_info()
```

## Documentation

```text
Provide information about available placeholder tokens and token types.

Tokens are placeholders that can be put into text by using the syntax
[type:token], where type is the machine-readable name of a token type, and
token is the machine-readable name of a token within this group. This hook
provides a list of types and tokens to be displayed on text editing screens,
so that people editing text can see what their token options are.

The actual token replacement is done by token_replace(), which invokes
hook_tokens(). Your module will need to implement that hook in order to
generate token replacements from the tokens defined here.

@return
  An associative array of available tokens and token types. The outer array
  has two components:
  - types: An associative array of token types (groups). Each token type is
    an associative array with the following components:
    - name: The translated human-readable short name of the token type.
    - description: A translated longer description of the token type.
    - needs-data: The type of data that must be provided to token_replace()
      in the $data argument (i.e., the key name in $data) in order for tokens
      of this type to be used in the $text being processed. For instance, if
      the token needs a node object, 'needs-data' should be 'node', and to
      use this token in token_replace(), the caller needs to supply a node
      object as $data['node']. Some token data can also be supplied
      indirectly; for instance, a node object in $data supplies a user object
      (the author of the node), allowing user tokens to be used when only
      a node data object is supplied.
  - tokens: An associative array of tokens. The outer array is keyed by the
    group name (the same key as in the types array). Within each group of
    tokens, each token item is keyed by the machine name of the token, and
    each token item has the following components:
    - name: The translated human-readable short name of the token.
    - description: A translated longer description of the token.
    - type (optional): A 'needs-data' data type supplied by this token, which
      should match a 'needs-data' value from another token type. For example,
      the node author token provides a user object, which can then be used
      for token replacement data in token_replace() without having to supply
      a separate user object.

@see hook_token_info_alter()
@see hook_tokens()
```

## Code

```php
function hook_token_info() {
  $type = array(
    'name' => t('Nodes'),
    'description' => t('Tokens related to individual nodes.'),
    'needs-data' => 'node',
  );

  // Core tokens for nodes.
  $node['nid'] = array(
    'name' => t("Node ID"),
    'description' => t("The unique ID of the node."),
  );
  $node['title'] = array(
    'name' => t("Title"),
    'description' => t("The title of the node."),
  );
  $node['edit-url'] = array(
    'name' => t("Edit URL"),
    'description' => t("The URL of the node's edit page."),
  );

  // Chained tokens for nodes.
  $node['created'] = array(
    'name' => t("Date created"),
    'description' => t("The date the node was posted."),
    'type' => 'date',
  );
  $node['author'] = array(
    'name' => t("Author"),
    'description' => t("The author of the node."),
    'type' => 'user',
  );

  return array(
    'types' => array('node' => $type),
    'tokens' => array('node' => $node),
  );
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_token_info()".

- [comment_token_info()](../../comment/comment.tokens.inc/comment_token_info.md) — `modules/comment/comment.tokens.inc`
- [node_token_info()](../../node/node.tokens.inc/node_token_info.md) — `modules/node/node.tokens.inc`
- [poll_token_info()](../../poll/poll.tokens.inc/poll_token_info.md) — `modules/poll/poll.tokens.inc`
- [statistics_token_info()](../../statistics/statistics.tokens.inc/statistics_token_info.md) — `modules/statistics/statistics.tokens.inc`
- [system_token_info()](../system.tokens.inc/system_token_info.md) — `modules/system/system.tokens.inc`
- [taxonomy_token_info()](../../taxonomy/taxonomy.tokens.inc/taxonomy_token_info.md) — `modules/taxonomy/taxonomy.tokens.inc`
- [user_token_info()](../../user/user.tokens.inc/user_token_info.md) — `modules/user/user.tokens.inc`

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
