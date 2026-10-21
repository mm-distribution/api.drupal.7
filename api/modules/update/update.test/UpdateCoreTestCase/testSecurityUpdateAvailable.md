# UpdateCoreTestCase::testSecurityUpdateAvailable()

- **Type:** Method
- **File:** [`modules/update/update.test`](../_file.md), lines 109–119 · [local source](../../../../../source/modules/update/update.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.test#L109-L119)
- **Class:** [UpdateCoreTestCase](../UpdateCoreTestCase.md)
- **Module/theme:** update

## Signature

```php
function testSecurityUpdateAvailable()
```

## Documentation

```text
Tests the Update Manager module when a security update is available.
```

## Code

```php
  function testSecurityUpdateAvailable() {
    $this->setSystemInfo7_0();
    $this->refreshUpdateStatus(array('drupal' => '2-sec'));
    $this->standardTests();
    $this->assertNoText(t('Up to date'));
    $this->assertNoText(t('Update available'));
    $this->assertText(t('Security update required!'));
    $this->assertRaw(l('7.2', 'http://example.com/drupal-7-2-release'), 'Link to release appears.');
    $this->assertRaw(l(t('Download'), 'http://example.com/drupal-7-2.tar.gz'), 'Link to download appears.');
    $this->assertRaw(l(t('Release notes'), 'http://example.com/drupal-7-2-release'), 'Link to release notes appears.');
  }
```

---
_Drupal 7.103 · [modules/update/update.test](https://github.com/drupal/drupal/blob/7.103/modules/update/update.test) · Licensed GPL-2.0-or-later (see LICENSE)._
