# Helper

- **Type:** Class
- **File:** [`misc/typo3/phar-stream-wrapper/src/Helper.php`](_file.md), lines 21–199 · [local source](../../../../../../source/misc/typo3/phar-stream-wrapper/src/Helper.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Helper.php#L21-L199)

## Signature

```php
class Helper
```

## Documentation

```text
Helper provides low-level tools on file name resolving. However it does not
(and should not) maintain any runtime state information. In order to resolve
Phar archive paths according resolvers have to be used.

@see \TYPO3\PharStreamWrapper\Resolvable::resolve()
```

## Methods (derived index)

- [resetOpCache()](Helper/resetOpCache.md)
- [determineBaseFile()](Helper/determineBaseFile.md) — Determines base file that can be accessed using the regular file system. For e.g. "phar:///home/user/bundle.phar/content.txt" that would result into "/home/user/bundle.phar".
- [hasPharPrefix()](Helper/hasPharPrefix.md)
- [removePharPrefix()](Helper/removePharPrefix.md)
- [normalizePath()](Helper/normalizePath.md) — Normalizes a path, removes phar:// prefix, fixes Windows directory separators. Result is without trailing slash.
- [normalizeWindowsPath()](Helper/normalizeWindowsPath.md) — Fixes a path for windows-backslashes and reduces double-slashes to single slashes
- [getCanonicalPath()](Helper/getCanonicalPath.md) — Resolves all dots, slashes and removes spaces after or before a path...
- [isAbsolutePath()](Helper/isAbsolutePath.md) — Checks if the $path is absolute or relative (detecting either '/' or 'x:/' as first part of string) and returns TRUE if so.
- [isWindows()](Helper/isWindows.md)

---
_Drupal 7.103 · [misc/typo3/phar-stream-wrapper/src/Helper.php](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Helper.php) · Licensed GPL-2.0-or-later (see LICENSE)._
