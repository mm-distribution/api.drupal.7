# SystemAuthorizeCase::testFileTransferHooks()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 2999–3009 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L2999-L3009)
- **Class:** [SystemAuthorizeCase](../SystemAuthorizeCase.md)
- **Module/theme:** system

## Signature

```php
function testFileTransferHooks()
```

## Documentation

```text
Tests the FileTransfer hooks
```

## Code

```php
  function testFileTransferHooks() {
    $page_title = $this->randomName(16);
    $this->drupalGetAuthorizePHP($page_title);
    $this->assertTitle(strtr('@title | Drupal', array('@title' => $page_title)), 'authorize.php page title is correct.');
    $this->assertNoText('It appears you have reached this page in error.');
    $this->assertText('To continue, provide your server connection details');
    // Make sure we see the new connection method added by system_test.
    $this->assertRaw('System Test FileTransfer');
    // Make sure the settings form callback works.
    $this->assertText('System Test Username');
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
