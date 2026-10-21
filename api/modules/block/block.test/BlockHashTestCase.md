# BlockHashTestCase

- **Type:** Class
- **File:** [`modules/block/block.test`](_file.md), lines 907–980 · [local source](../../../../source/modules/block/block.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.test#L907-L980)
- **Module/theme:** block

## Signature

```php
class BlockHashTestCase extends DrupalWebTestCase
```

## Documentation

```text
Tests that block rehashing works correctly.
```

## Methods (derived index)

- [getInfo()](BlockHashTestCase/getInfo.md)
- [setUp()](BlockHashTestCase/setUp.md)
- [testBlockRehash()](BlockHashTestCase/testBlockRehash.md) — Tests that block rehashing does not write to the database too often.
- [doRehash()](BlockHashTestCase/doRehash.md) — Performs a block rehash and checks several related assertions.
- [assertWeight()](BlockHashTestCase/assertWeight.md) — Asserts that the block_test module's block has a given weight.

---
_Drupal 7.103 · [modules/block/block.test](https://github.com/drupal/drupal/blob/7.103/modules/block/block.test) · Licensed GPL-2.0-or-later (see LICENSE)._
