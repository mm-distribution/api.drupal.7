# TokenScanTest::testTokenScan()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 3061–3073 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L3061-L3073)
- **Class:** [TokenScanTest](../TokenScanTest.md)
- **Module/theme:** system

## Signature

```php
function testTokenScan()
```

## Documentation

```text
Scans dummy text, then tests the output.
```

## Code

```php
  function testTokenScan() {
    // Define text with valid and not valid, fake and existing token-like
    // strings.
    $text = 'First a [valid:simple], but dummy token, and a dummy [valid:token with: spaces].';
    $text .= 'Then a [not valid:token].';
    $text .= 'Last an existing token: [node:author:name].';
    $token_wannabes = token_scan($text);

    $this->assertTrue(isset($token_wannabes['valid']['simple']), 'A simple valid token has been matched.');
    $this->assertTrue(isset($token_wannabes['valid']['token with: spaces']), 'A valid token with space characters in the token name has been matched.');
    $this->assertFalse(isset($token_wannabes['not valid']), 'An invalid token with spaces in the token type has not been matched.');
    $this->assertTrue(isset($token_wannabes['node']), 'An existing valid token has been matched.');
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
