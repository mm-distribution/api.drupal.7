# Helper::getCanonicalPath()

- **Type:** Method
- **File:** [`misc/typo3/phar-stream-wrapper/src/Helper.php`](../_file.md), lines 120–172 · [local source](../../../../../../../source/misc/typo3/phar-stream-wrapper/src/Helper.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Helper.php#L120-L172)
- **Class:** [Helper](../Helper.md)

## Signature

```php
private static function getCanonicalPath($path)
```

## Documentation

```text
Resolves all dots, slashes and removes spaces after or before a path...

@param string $path Input string
@return string Canonical path, always without trailing slash
```

## Code

```php
    private static function getCanonicalPath($path)
    {
        $path = static::normalizeWindowsPath($path);

        $absolutePathPrefix = '';
        if (static::isAbsolutePath($path)) {
            if (static::isWindows() && strpos($path, ':/') === 1) {
                $absolutePathPrefix = substr($path, 0, 3);
                $path = substr($path, 3);
            } else {
                $path = ltrim($path, '/');
                $absolutePathPrefix = '/';
            }
        }

        $pathParts = explode('/', $path);
        $pathPartsLength = count($pathParts);
        for ($partCount = 0; $partCount < $pathPartsLength; $partCount++) {
            // double-slashes in path: remove element
            if ($pathParts[$partCount] === '') {
                array_splice($pathParts, $partCount, 1);
                $partCount--;
                $pathPartsLength--;
            }
            // "." in path: remove element
            if ((isset($pathParts[$partCount]) ? $pathParts[$partCount] : '') === '.') {
                array_splice($pathParts, $partCount, 1);
                $partCount--;
                $pathPartsLength--;
            }
            // ".." in path:
            if ((isset($pathParts[$partCount]) ? $pathParts[$partCount] : '') === '..') {
                if ($partCount === 0) {
                    array_splice($pathParts, $partCount, 1);
                    $partCount--;
                    $pathPartsLength--;
                } elseif ($partCount >= 1) {
                    // Rremove this and previous element
                    array_splice($pathParts, $partCount - 1, 2);
                    $partCount -= 2;
                    $pathPartsLength -= 2;
                } elseif ($absolutePathPrefix) {
                    // can't go higher than root dir
                    // simply remove this part and continue
                    array_splice($pathParts, $partCount, 1);
                    $partCount--;
                    $pathPartsLength--;
                }
            }
        }

        return $absolutePathPrefix . implode('/', $pathParts);
    }
```

---
_Drupal 7.103 · [misc/typo3/phar-stream-wrapper/src/Helper.php](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Helper.php) · Licensed GPL-2.0-or-later (see LICENSE)._
