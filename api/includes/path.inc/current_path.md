# current_path()

- **Type:** Function
- **File:** [`includes/path.inc`](_file.md), lines 355–357 · [local source](../../../source/includes/path.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/path.inc#L355-L357)

## Signature

```php
function current_path()
```

## Documentation

```text
Return the current URL path of the page being viewed.

Examples:
- http://example.com/node/306 returns "node/306".
- http://example.com/drupalfolder/node/306 returns "node/306" while
  base_path() returns "/drupalfolder/".
- http://example.com/path/alias (which is a path alias for node/306) returns
  "node/306" as opposed to the path alias.

This function is not available in hook_boot() so use $_GET['q'] instead.
However, be careful when doing that because in the case of Example #3
$_GET['q'] will contain "path/alias". If "node/306" is needed, calling
drupal_bootstrap(DRUPAL_BOOTSTRAP_FULL) makes this function available.

@return
  The current Drupal URL path. The path is untrusted user input and must be
  treated as such.

@see request_path()
```

## Code

```php
function current_path() {
  return $_GET['q'];
}
```

---
_Drupal 7.103 · [includes/path.inc](https://github.com/drupal/drupal/blob/7.103/includes/path.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
