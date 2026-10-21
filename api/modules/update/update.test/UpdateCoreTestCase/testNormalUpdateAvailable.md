# UpdateCoreTestCase::testNormalUpdateAvailable()

- **Type:** Method
- **File:** [`modules/update/update.test`](../_file.md), lines 94–104 · [local source](../../../../../source/modules/update/update.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.test#L94-L104)
- **Class:** [UpdateCoreTestCase](../UpdateCoreTestCase.md)
- **Module/theme:** update

## Signature

```php
function testNormalUpdateAvailable()
```

## Documentation

```text
Tests the Update Manager module when one normal update is available.
```

## Code

```php
  function testNormalUpdateAvailable() {
    $this->setSystemInfo7_0();
    $this->refreshUpdateStatus(array('drupal' => '1'));
    $this->standardTests();
    $this->assertNoText(t('Up to date'));
    $this->assertText(t('Update available'));
    $this->assertNoText(t('Security update required!'));
    $this->assertRaw(l('7.1', 'http://example.com/drupal-7-1-release'), 'Link to release appears.');
    $this->assertRaw(l(t('Download'), 'http://example.com/drupal-7-1.tar.gz'), 'Link to download appears.');
    $this->assertRaw(l(t('Release notes'), 'http://example.com/drupal-7-1-release'), 'Link to release notes appears.');
  }
```

---
_Drupal 7.103 · [modules/update/update.test](https://github.com/drupal/drupal/blob/7.103/modules/update/update.test) · Licensed GPL-2.0-or-later (see LICENSE)._
