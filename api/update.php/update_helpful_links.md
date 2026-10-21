# update_helpful_links()

- **Type:** Function
- **File:** [`update.php`](_file.md), lines 149–155 · [local source](../../source/update.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/update.php#L149-L155)

## Signature

```php
function update_helpful_links()
```

## Documentation

```text
Provides links to the homepage and administration pages.
```

## Code

```php
function update_helpful_links() {
  $links[] = '<a href="' . base_path() . '">Front page</a>';
  if (user_access('access administration pages')) {
    $links[] = '<a href="' . base_path() . '?q=admin">Administration pages</a>';
  }
  return $links;
}
```

---
_Drupal 7.103 · [update.php](https://github.com/drupal/drupal/blob/7.103/update.php) · Licensed GPL-2.0-or-later (see LICENSE)._
