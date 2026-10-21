# PharInvocationResolver::resolvePossibleAlias()

- **Type:** Method
- **File:** [`misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocationResolver.php`](../_file.md), lines 172–176 · [local source](../../../../../../../../source/misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocationResolver.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocationResolver.php#L172-L176)
- **Class:** [PharInvocationResolver](../PharInvocationResolver.md)

## Signature

```php
private function resolvePossibleAlias($path)
```

## Documentation

```text
@param string $path
@return null|string
```

## Code

```php
    private function resolvePossibleAlias($path)
    {
        $normalizedPath = Helper::normalizePath($path);
        return strstr($normalizedPath, '/', true) ?: null;
    }
```

---
_Drupal 7.103 · [misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocationResolver.php](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocationResolver.php) · Licensed GPL-2.0-or-later (see LICENSE)._
