# vancode2int()

- **Type:** Function
- **File:** [`modules/comment/comment.module`](_file.md), lines 2528–2530 · [local source](../../../../source/modules/comment/comment.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module#L2528-L2530)
- **Module/theme:** comment

## Signature

```php
function vancode2int($c = '00')
```

## Documentation

```text
Decode vancode back to an integer.
```

## Code

```php
function vancode2int($c = '00') {
  return base_convert(substr($c, 1), 36, 10);
}
```

---
_Drupal 7.103 · [modules/comment/comment.module](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module) · Licensed GPL-2.0-or-later (see LICENSE)._
