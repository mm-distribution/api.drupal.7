# BlockHashTestCase::testBlockRehash()

- **Type:** Method
- **File:** [`modules/block/block.test`](../_file.md), lines 923–943 · [local source](../../../../../source/modules/block/block.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.test#L923-L943)
- **Class:** [BlockHashTestCase](../BlockHashTestCase.md)
- **Module/theme:** block

## Signature

```php
function testBlockRehash()
```

## Documentation

```text
Tests that block rehashing does not write to the database too often.
```

## Code

```php
  function testBlockRehash() {
    // No hook_block_info_alter(), no save.
    $this->doRehash();
    module_enable(array('block_test'), FALSE);
    // Save the new blocks, check that the new blocks exist by checking weight.
    _block_rehash();
    $this->assertWeight(0);
    // Now hook_block_info_alter() exists but no blocks are saved on a second
    // rehash.
    $this->doRehash();
    $this->assertWeight(0);
    // Now hook_block_info_alter() exists and is changing one block which
    // should be saved.
    $GLOBALS['conf']['block_test_info_alter'] = 1;
    $this->doRehash(TRUE);
    $this->assertWeight(10000);
    // Now hook_block_info_alter() exists but already changed the block's
    // weight before, so it should not be saved again.
    $this->doRehash();
    $this->assertWeight(10000);
  }
```

---
_Drupal 7.103 · [modules/block/block.test](https://github.com/drupal/drupal/blob/7.103/modules/block/block.test) · Licensed GPL-2.0-or-later (see LICENSE)._
