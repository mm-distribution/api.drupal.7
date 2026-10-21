# ForumIndexTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/forum/forum.test`](../_file.md), lines 676–682 · [local source](../../../../../source/modules/forum/forum.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.test#L676-L682)
- **Class:** [ForumIndexTestCase](../ForumIndexTestCase.md)
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
      'name' => 'Forum index',
      'description' => 'Tests the forum index listing.',
      'group' => 'Forum',
    );
  }
```

---
_Drupal 7.103 · [modules/forum/forum.test](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.test) · Licensed GPL-2.0-or-later (see LICENSE)._
