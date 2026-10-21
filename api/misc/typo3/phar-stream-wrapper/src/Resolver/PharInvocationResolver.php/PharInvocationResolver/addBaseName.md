# PharInvocationResolver::addBaseName()

- **Type:** Method
- **File:** [`misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocationResolver.php`](../_file.md), lines 219–227 · [local source](../../../../../../../../source/misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocationResolver.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocationResolver.php#L219-L227)
- **Class:** [PharInvocationResolver](../PharInvocationResolver.md)

## Signature

```php
private function addBaseName($baseName)
```

## Documentation

```text
@param string $baseName
```

## Code

```php
    private function addBaseName($baseName)
    {
        if (isset($this->baseNames[$baseName])) {
            return;
        }
        $this->baseNames[$baseName] = Helper::normalizeWindowsPath(
            realpath($baseName)
        );
    }
```

---
_Drupal 7.103 · [misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocationResolver.php](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocationResolver.php) · Licensed GPL-2.0-or-later (see LICENSE)._
