# int2vancode()

- **Type:** Function
- **File:** [`modules/comment/comment.module`](_file.md), lines 2518–2523 · [local source](../../../../source/modules/comment/comment.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module#L2518-L2523)
- **Module/theme:** comment

## Signature

```php
function int2vancode($i = 0)
```

## Documentation

```text
Generate vancode.

Consists of a leading character indicating length, followed by N digits
with a numerical value in base 36. Vancodes can be sorted as strings
without messing up numerical order.

It goes:
00, 01, 02, ..., 0y, 0z,
110, 111, ... , 1zy, 1zz,
2100, 2101, ..., 2zzy, 2zzz,
31000, 31001, ...
```

## Code

```php
function int2vancode($i = 0) {
  $num = base_convert((int) $i, 10, 36);
  $length = strlen($num);

  return chr($length + ord('0') - 1) . $num;
}
```

---
_Drupal 7.103 · [modules/comment/comment.module](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module) · Licensed GPL-2.0-or-later (see LICENSE)._
