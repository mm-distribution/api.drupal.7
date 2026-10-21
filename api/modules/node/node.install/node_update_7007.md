# node_update_7007()

- **Type:** Function
- **File:** [`modules/node/node.install`](_file.md), lines 792–794 · [local source](../../../../source/modules/node/node.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.install#L792-L794)
- **Module/theme:** node
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function node_update_7007()
```

## Documentation

```text
Remove column min_word_count.
```

## Code

```php
function node_update_7007() {
  db_drop_field('node_type', 'min_word_count');
}
```

---
_Drupal 7.103 · [modules/node/node.install](https://github.com/drupal/drupal/blob/7.103/modules/node/node.install) · Licensed GPL-2.0-or-later (see LICENSE)._
