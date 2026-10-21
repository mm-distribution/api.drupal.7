# hook_search_access()

- **Type:** Hook (documentation function)
- **File:** [`modules/search/search.api.php`](_file.md), lines 60–62 · [local source](../../../../source/modules/search/search.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.api.php#L60-L62)
- **Module/theme:** search
- **Topics:** [hooks](../../../topics/hooks.md), [search](../../../topics/search.md)

## Signature

```php
function hook_search_access()
```

## Documentation

```text
Define access to a custom search routine.

This hook allows a module to define permissions for a search tab.

@ingroup search
```

## Code

```php
function hook_search_access() {
  return user_access('access content');
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_search_access()".

- [node_search_access()](../../node/node.module/node_search_access.md) — `modules/node/node.module`
- [user_search_access()](../../user/user.module/user_search_access.md) — `modules/user/user.module`

---
_Drupal 7.103 · [modules/search/search.api.php](https://github.com/drupal/drupal/blob/7.103/modules/search/search.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
