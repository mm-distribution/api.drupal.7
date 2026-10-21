# NodeAccessBaseTableTestCase

- **Type:** Class
- **File:** [`modules/node/node.test`](_file.md), lines 1159–1315 · [local source](../../../../source/modules/node/node.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test#L1159-L1315)
- **Module/theme:** node

## Signature

```php
class NodeAccessBaseTableTestCase extends DrupalWebTestCase
```

## Documentation

```text
Tests for Node Access with a non-node base table.
```

## Properties

### $nodesByUser

```php
protected $nodesByUser;
```

### $webUser

```php
protected $webUser;
```

### $publicTid

```php
protected $publicTid;
```

### $privateTid

```php
protected $privateTid;
```

### $nids_visible

```php
protected $nids_visible;
```

## Methods (derived index)

- [getInfo()](NodeAccessBaseTableTestCase/getInfo.md)
- [setUp()](NodeAccessBaseTableTestCase/setUp.md)
- [testNodeAccessBasic()](NodeAccessBaseTableTestCase/testNodeAccessBasic.md) — Tests the "private" node access functionality.
- [assertTaxonomyPage()](NodeAccessBaseTableTestCase/assertTaxonomyPage.md) — Checks taxonomy/term listings to ensure only accessible nodes are listed.

---
_Drupal 7.103 · [modules/node/node.test](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test) · Licensed GPL-2.0-or-later (see LICENSE)._
