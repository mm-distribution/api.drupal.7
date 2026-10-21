# ForumTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/forum/forum.test`](../_file.md), lines 58–64 · [local source](../../../../../source/modules/forum/forum.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.test#L58-L64)
- **Class:** [ForumTestCase](../ForumTestCase.md)
- **Module/theme:** forum

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
      'name' => 'Forum functionality',
      'description' => 'Create, view, edit, delete, and change forum entries and verify its consistency in the database.',
      'group' => 'Forum',
    );
  }
```

---
_Drupal 7.103 · [modules/forum/forum.test](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.test) · Licensed GPL-2.0-or-later (see LICENSE)._
