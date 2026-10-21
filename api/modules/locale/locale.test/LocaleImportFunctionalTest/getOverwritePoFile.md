# LocaleImportFunctionalTest::getOverwritePoFile()

- **Type:** Method
- **File:** [`modules/locale/locale.test`](../_file.md), lines 1228–1244 · [local source](../../../../../source/modules/locale/locale.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test#L1228-L1244)
- **Class:** [LocaleImportFunctionalTest](../LocaleImportFunctionalTest.md)
- **Module/theme:** locale

## Signature

```php
function getOverwritePoFile()
```

## Documentation

```text
Helper function that returns a proper .po file, for testing overwriting
existing translations.
```

## Code

```php
  function getOverwritePoFile() {
    return <<< EOF
msgid ""
msgstr ""
"Project-Id-Version: Drupal 7\\n"
"MIME-Version: 1.0\\n"
"Content-Type: text/plain; charset=UTF-8\\n"
"Content-Transfer-Encoding: 8bit\\n"
"Plural-Forms: nplurals=3; plural=n%10==1 && n%100!=11 ? 0 : n%10>=2 && n%10<=4 && (n%100<10 || n%100>=20) ? 1 : 2;\\n"

msgid "Monday"
msgstr "Montag"

msgid "Day"
msgstr "Jour"
EOF;
  }
```

---
_Drupal 7.103 · [modules/locale/locale.test](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test) · Licensed GPL-2.0-or-later (see LICENSE)._
