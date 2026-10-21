# FilterFormatAccessTestCase

- **Type:** Class
- **File:** [`modules/filter/filter.test`](_file.md), lines 437–736 · [local source](../../../../source/modules/filter/filter.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.test#L437-L736)
- **Module/theme:** filter

## Signature

```php
class FilterFormatAccessTestCase extends DrupalWebTestCase
```

## Documentation

```text
Tests the filter format access functionality in the Filter module.
```

## Properties

### $admin_user

```php
protected $admin_user;
```

```text
A user with administrative permissions.

@var object
```

### $filter_admin_user

```php
protected $filter_admin_user;
```

```text
A user with 'administer filters' permission.

@var object
```

### $web_user

```php
protected $web_user;
```

```text
A user with permission to create and edit own content.

@var object
```

### $allowed_format

```php
protected $allowed_format;
```

```text
An object representing an allowed text format.

@var object
```

### $disallowed_format

```php
protected $disallowed_format;
```

```text
An object representing a disallowed text format.

@var object
```

## Methods (derived index)

- [getInfo()](FilterFormatAccessTestCase/getInfo.md)
- [setUp()](FilterFormatAccessTestCase/setUp.md)
- [testFormatPermissions()](FilterFormatAccessTestCase/testFormatPermissions.md) — Tests the Filter format access permissions functionality.
- [testFormatRoles()](FilterFormatAccessTestCase/testFormatRoles.md) — Tests if text format is available to a role.
- [testFormatWidgetPermissions()](FilterFormatAccessTestCase/testFormatWidgetPermissions.md) — Tests editing a page using a disallowed text format.
- [resetFilterCaches()](FilterFormatAccessTestCase/resetFilterCaches.md) — Rebuilds text format and permission caches in the thread running the tests.

---
_Drupal 7.103 · [modules/filter/filter.test](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.test) · Licensed GPL-2.0-or-later (see LICENSE)._
