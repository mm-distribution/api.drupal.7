# BlogTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/blog/blog.test`](../_file.md), lines 13–19 · [local source](../../../../../source/modules/blog/blog.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/blog/blog.test#L13-L19)
- **Class:** [BlogTestCase](../BlogTestCase.md)
- **Module/theme:** blog

## Signature

```php
public static function getInfo()
```

## Documentation

_No docblock in source._

## Code

```php
  public static function getInfo() {
    return array(
      'name' => 'Blog functionality',
      'description' => 'Create, view, edit, delete, and change blog entries and verify its consistency in the database.',
      'group' => 'Blog',
    );
  }
```

---
_Drupal 7.103 · [modules/blog/blog.test](https://github.com/drupal/drupal/blob/7.103/modules/blog/blog.test) · Licensed GPL-2.0-or-later (see LICENSE)._
