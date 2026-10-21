# NodeEntityFieldQueryAlter

- **Type:** Class
- **File:** [`modules/node/node.test`](_file.md), lines 2457–2520 · [local source](../../../../source/modules/node/node.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test#L2457-L2520)
- **Module/theme:** node

## Signature

```php
class NodeEntityFieldQueryAlter extends DrupalWebTestCase
```

## Documentation

```text
Tests node_query_entity_field_access_alter().
```

## Properties

### $accessUser

```php
protected $accessUser;
```

```text
User with permission to view content.

@var object
```

### $noAccessUser

```php
protected $noAccessUser;
```

```text
User without permission to view content.

@var object
```

## Methods (derived index)

- [getInfo()](NodeEntityFieldQueryAlter/getInfo.md)
- [setUp()](NodeEntityFieldQueryAlter/setUp.md)
- [testNodeQueryAlterWithUI()](NodeEntityFieldQueryAlter/testNodeQueryAlterWithUI.md) — Tests that node access permissions are followed.

---
_Drupal 7.103 · [modules/node/node.test](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test) · Licensed GPL-2.0-or-later (see LICENSE)._
