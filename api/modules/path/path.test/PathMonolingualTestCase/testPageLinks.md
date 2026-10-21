# PathMonolingualTestCase::testPageLinks()

- **Type:** Method
- **File:** [`modules/path/path.test`](../_file.md), lines 604–615 · [local source](../../../../../source/modules/path/path.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/path/path.test#L604-L615)
- **Class:** [PathMonolingualTestCase](../PathMonolingualTestCase.md)
- **Module/theme:** path

## Signature

```php
function testPageLinks()
```

## Documentation

```text
Verifies that links do not have language prefixes in them.
```

## Code

```php
  function testPageLinks() {
    // Navigate to 'admin/config' path.
    $this->drupalGet('admin/config');

    // Verify that links in this page do not have a 'fr/' prefix.
    $this->assertNoLinkByHref('/fr/', 'Links do not contain language prefix');

    // Verify that links in this page can be followed and work.
    $this->clickLink(t('Languages'));
    $this->assertResponse(200, 'Clicked link results in a valid page');
    $this->assertText(t('Add language'), 'Page contains the add language text');
  }
```

---
_Drupal 7.103 · [modules/path/path.test](https://github.com/drupal/drupal/blob/7.103/modules/path/path.test) · Licensed GPL-2.0-or-later (see LICENSE)._
