# BlockHashTestCase::doRehash()

- **Type:** Method
- **File:** [`modules/block/block.test`](../_file.md), lines 953–967 · [local source](../../../../../source/modules/block/block.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.test#L953-L967)
- **Class:** [BlockHashTestCase](../BlockHashTestCase.md)
- **Module/theme:** block

## Signature

```php
function doRehash($alter_active = FALSE)
```

## Documentation

```text
Performs a block rehash and checks several related assertions.

@param $alter_active
  Set to TRUE if the block_test module's hook_block_info_alter()
  implementation is expected to make a change that results in an existing
  block needing to be resaved to the database. Defaults to FALSE.
```

## Code

```php
  function doRehash($alter_active = FALSE) {
    $saves = 0;
    foreach (_block_rehash() as $block) {
      $module = $block['module'];
      $delta = $block['delta'];
      if ($alter_active && $module == 'block_test' && $delta == 'test_html_id') {
        $this->assertFalse(empty($block['saved']), "$module $delta saved");
        $saves++;
      }
      else {
        $this->assertTrue(empty($block['saved']), "$module $delta not saved");
      }
    }
    $this->assertEqual($alter_active, $saves);
  }
```

---
_Drupal 7.103 · [modules/block/block.test](https://github.com/drupal/drupal/blob/7.103/modules/block/block.test) · Licensed GPL-2.0-or-later (see LICENSE)._
