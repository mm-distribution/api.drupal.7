# PharInvocationResolver::resolveBaseName()

- **Type:** Method
- **File:** [`misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocationResolver.php`](../_file.md), lines 117–166 · [local source](../../../../../../../../source/misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocationResolver.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocationResolver.php#L117-L166)
- **Class:** [PharInvocationResolver](../PharInvocationResolver.md)

## Signature

```php
private function resolveBaseName($path, $flags)
```

## Documentation

```text
@param string $path
@param int $flags
@return null|string
```

## Code

```php
    private function resolveBaseName($path, $flags)
    {
        $baseName = $this->findInBaseNames($path);
        if ($baseName !== null) {
            return $baseName;
        }

        $baseName = Helper::determineBaseFile($path);
        if ($baseName !== null) {
            $this->addBaseName($baseName);
            return $baseName;
        }

        $possibleAlias = $this->resolvePossibleAlias($path);
        if (!($flags & static::RESOLVE_ALIAS) || $possibleAlias === null) {
            return null;
        }

        $trace = debug_backtrace();
        foreach ($trace as $item) {
            if (!isset($item['function']) || !isset($item['args'][0])
                || !in_array($item['function'], $this->invocationFunctionNames, true)) {
                continue;
            }
            $currentPath = $item['args'][0];
            if (Helper::hasPharPrefix($currentPath)) {
                continue;
            }
            $currentBaseName = Helper::determineBaseFile($currentPath);
            if ($currentBaseName === null) {
                continue;
            }
            // ensure the possible alias name (how we have been called initially) matches
            // the resolved alias name that was retrieved by the current possible base name
            try {
                $reader = new Reader($currentBaseName);
                $currentAlias = $reader->resolveContainer()->getAlias();
            } catch (ReaderException $exception) {
                // most probably that was not a Phar file
                continue;
            }
            if (empty($currentAlias) || $currentAlias !== $possibleAlias) {
                continue;
            }
            $this->addBaseName($currentBaseName);
            return $currentBaseName;
        }

        return null;
    }
```

---
_Drupal 7.103 · [misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocationResolver.php](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocationResolver.php) · Licensed GPL-2.0-or-later (see LICENSE)._
