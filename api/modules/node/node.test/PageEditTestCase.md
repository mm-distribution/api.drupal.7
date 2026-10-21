# PageEditTestCase

- **Type:** Class
- **File:** [`modules/node/node.test`](_file.md), lines 303–445 · [local source](../../../../source/modules/node/node.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test#L303-L445)
- **Module/theme:** node

## Signature

```php
class PageEditTestCase extends DrupalWebTestCase
```

## Documentation

```text
Tests the node edit functionality.
```

## Properties

### $web_user

```php
protected $web_user;
```

```text
A user with permission to create and edit own page content.

@var object
```

### $admin_user

```php
protected $admin_user;
```

```text
A user with permission to bypass node access and administer nodes.

@var object
```

## Methods (derived index)

- [getInfo()](PageEditTestCase/getInfo.md)
- [setUp()](PageEditTestCase/setUp.md)
- [testPageEdit()](PageEditTestCase/testPageEdit.md) — Checks node edit functionality.
- [testPageAuthoredBy()](PageEditTestCase/testPageAuthoredBy.md) — Tests changing a node's "authored by" field.

---
_Drupal 7.103 · [modules/node/node.test](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test) · Licensed GPL-2.0-or-later (see LICENSE)._
