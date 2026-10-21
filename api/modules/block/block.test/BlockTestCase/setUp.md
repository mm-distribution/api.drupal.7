# BlockTestCase::setUp()

- **Type:** Method
- **File:** [`modules/block/block.test`](../_file.md), lines 20–40 · [local source](../../../../../source/modules/block/block.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.test#L20-L40)
- **Class:** [BlockTestCase](../BlockTestCase.md)
- **Module/theme:** block

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    parent::setUp();

    // Create and log in an administrative user having access to the Full HTML
    // text format.
    $full_html_format = filter_format_load('full_html');
    $this->admin_user = $this->drupalCreateUser(array(
      'administer blocks',
      filter_permission_name($full_html_format),
      'access administration pages',
    ));
    $this->drupalLogin($this->admin_user);

    // Define the existing regions
    $this->regions = array();
    $this->regions[] = 'header';
    $this->regions[] = 'sidebar_first';
    $this->regions[] = 'content';
    $this->regions[] = 'sidebar_second';
    $this->regions[] = 'footer';
  }
```

---
_Drupal 7.103 · [modules/block/block.test](https://github.com/drupal/drupal/blob/7.103/modules/block/block.test) · Licensed GPL-2.0-or-later (see LICENSE)._
