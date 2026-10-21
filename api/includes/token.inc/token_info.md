# token_info()

- **Type:** Function
- **File:** [`includes/token.inc`](_file.md), lines 257–264 · [local source](../../../source/includes/token.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/token.inc#L257-L264)

## Signature

```php
function token_info()
```

## Documentation

```text
Returns metadata describing supported tokens.

The metadata array contains token type, name, and description data as well
as an optional pointer indicating that the token chains to another set of
tokens.

For example:
@code
  $data['types']['node'] = array(
    'name' => t('Nodes'),
    'description' => t('Tokens related to node objects.'),
  );
  $data['tokens']['node']['title'] = array(
    'name' => t('Title'),
    'description' => t('The title of the current node.'),
  );
  $data['tokens']['node']['author'] = array(
    'name' => t('Author'),
    'description' => t('The author of the current node.'),
    'type' => 'user',
  );
@endcode

@return
  An associative array of token information, grouped by token type.
```

## Code

```php
function token_info() {
  $data = &drupal_static(__FUNCTION__);
  if (!isset($data)) {
    $data = module_invoke_all('token_info');
    drupal_alter('token_info', $data);
  }
  return $data;
}
```

---
_Drupal 7.103 · [includes/token.inc](https://github.com/drupal/drupal/blob/7.103/includes/token.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
