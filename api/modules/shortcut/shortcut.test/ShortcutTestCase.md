# ShortcutTestCase

- **Type:** Class
- **File:** [`modules/shortcut/shortcut.test`](_file.md), lines 11–97 · [local source](../../../../source/modules/shortcut/shortcut.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.test#L11-L97)
- **Module/theme:** shortcut

## Signature

```php
class ShortcutTestCase extends DrupalWebTestCase
```

## Documentation

```text
Defines base class for shortcut test cases.
```

## Properties

### $admin_user

```php
protected $admin_user;
```

```text
User with permission to administer shortcuts.
```

### $shortcut_user

```php
protected $shortcut_user;
```

```text
User with permission to use shortcuts, but not administer them.
```

### $node

```php
protected $node;
```

```text
Generic node used for testing.
```

### $set

```php
protected $set;
```

```text
Site-wide default shortcut set.
```

## Methods (derived index)

- [setUp()](ShortcutTestCase/setUp.md)
- [generateShortcutSet()](ShortcutTestCase/generateShortcutSet.md) — Creates a generic shortcut set.
- [generateShortcutLink()](ShortcutTestCase/generateShortcutLink.md) — Creates a generic shortcut link.
- [getShortcutInformation()](ShortcutTestCase/getShortcutInformation.md) — Extracts information from shortcut set links.

---
_Drupal 7.103 · [modules/shortcut/shortcut.test](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.test) · Licensed GPL-2.0-or-later (see LICENSE)._
