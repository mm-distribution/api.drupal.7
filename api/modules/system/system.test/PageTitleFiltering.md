# PageTitleFiltering

- **Type:** Class
- **File:** [`modules/system/system.test`](_file.md), lines 1584–1686 · [local source](../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L1584-L1686)
- **Module/theme:** system

## Signature

```php
class PageTitleFiltering extends DrupalWebTestCase
```

## Documentation

_No docblock in source._

## Properties

### $content_user

```php
protected $content_user;
```

### $saved_title

```php
protected $saved_title;
```

## Methods (derived index)

- [getInfo()](PageTitleFiltering/getInfo.md) — Implement getInfo().
- [setUp()](PageTitleFiltering/setUp.md) — Implement setUp().
- [tearDown()](PageTitleFiltering/tearDown.md) — Reset page title.
- [testTitleTags()](PageTitleFiltering/testTitleTags.md) — Tests the handling of HTML by drupal_set_title() and drupal_get_title()
- [testTitleXSS()](PageTitleFiltering/testTitleXSS.md) — Test if the title of the site is XSS proof.

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
