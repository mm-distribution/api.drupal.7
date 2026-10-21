# PharInvocationResolver::findInBaseNames()

- **Type:** Method
- **File:** [`misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocationResolver.php`](../_file.md), lines 196–214 · [local source](../../../../../../../../source/misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocationResolver.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocationResolver.php#L196-L214)
- **Class:** [PharInvocationResolver](../PharInvocationResolver.md)

## Signature

```php
private function findInBaseNames($path)
```

## Documentation

```text
@param string $path
@return null|string
```

## Code

```php
    private function findInBaseNames($path)
    {
        // return directly if the resolved base name was submitted
        if (in_array($path, $this->baseNames, true)) {
            return $path;
        }

        $parts = explode('/', Helper::normalizePath($path));

        while (count($parts)) {
            $currentPath = implode('/', $parts);
            if (isset($this->baseNames[$currentPath])) {
                return $currentPath;
            }
            array_pop($parts);
        }

        return null;
    }
```

---
_Drupal 7.103 · [misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocationResolver.php](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocationResolver.php) · Licensed GPL-2.0-or-later (see LICENSE)._
