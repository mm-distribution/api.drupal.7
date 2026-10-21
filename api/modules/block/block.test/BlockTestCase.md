# BlockTestCase

- **Type:** Class
- **File:** [`modules/block/block.test`](_file.md), lines 8–381 · [local source](../../../../source/modules/block/block.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.test#L8-L381)
- **Module/theme:** block

## Signature

```php
class BlockTestCase extends DrupalWebTestCase
```

## Documentation

_No docblock in source._

## Properties

### $regions

```php
protected $regions;
```

### $admin_user

```php
protected $admin_user;
```

## Methods (derived index)

- [getInfo()](BlockTestCase/getInfo.md)
- [setUp()](BlockTestCase/setUp.md)
- [testCustomBlock()](BlockTestCase/testCustomBlock.md) — Test creating custom block, moving it to a specific region and then deleting it.
- [testCustomBlockFormat()](BlockTestCase/testCustomBlockFormat.md) — Test creating custom block using Full HTML.
- [testBlockVisibility()](BlockTestCase/testBlockVisibility.md) — Test block visibility.
- [testBlockVisibilityListedEmpty()](BlockTestCase/testBlockVisibilityListedEmpty.md) — Test block visibility when using "pages" restriction but leaving "pages" textarea empty
- [testBlockVisibilityPerUser()](BlockTestCase/testBlockVisibilityPerUser.md) — Test user customization of block visibility.
- [testBlock()](BlockTestCase/testBlock.md) — Test configuring and moving a module-define block to specific regions.
- [moveBlockToRegion()](BlockTestCase/moveBlockToRegion.md)
- [testBlockRehash()](BlockTestCase/testBlockRehash.md) — Test _block_rehash().

---
_Drupal 7.103 · [modules/block/block.test](https://github.com/drupal/drupal/blob/7.103/modules/block/block.test) · Licensed GPL-2.0-or-later (see LICENSE)._
