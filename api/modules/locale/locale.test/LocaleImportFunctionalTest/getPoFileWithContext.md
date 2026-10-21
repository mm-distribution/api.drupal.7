# LocaleImportFunctionalTest::getPoFileWithContext()

- **Type:** Method
- **File:** [`modules/locale/locale.test`](../_file.md), lines 1249–1268 · [local source](../../../../../source/modules/locale/locale.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test#L1249-L1268)
- **Class:** [LocaleImportFunctionalTest](../LocaleImportFunctionalTest.md)
- **Module/theme:** locale

## Signature

```php
function getPoFileWithContext()
```

## Documentation

```text
Helper function that returns a .po file with context.
```

## Code

```php
  function getPoFileWithContext() {
    // Croatian (code hr) is one of the languages that have a different
    // form for the full name and the abbreviated name for the month May.
    return <<< EOF
msgid ""
msgstr ""
"Project-Id-Version: Drupal 7\\n"
"MIME-Version: 1.0\\n"
"Content-Type: text/plain; charset=UTF-8\\n"
"Content-Transfer-Encoding: 8bit\\n"
"Plural-Forms: nplurals=3; plural=n%10==1 && n%100!=11 ? 0 : n%10>=2 && n%10<=4 && (n%100<10 || n%100>=20) ? 1 : 2;\\n"

msgctxt "Long month name"
msgid "May"
msgstr "Svibanj"

msgid "May"
msgstr "Svi."
EOF;
  }
```

---
_Drupal 7.103 · [modules/locale/locale.test](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test) · Licensed GPL-2.0-or-later (see LICENSE)._
