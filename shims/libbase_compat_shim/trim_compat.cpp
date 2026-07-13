// Samsung's TZ KeyMint blobs were built against an older libbase that
// exported a non-template android::base::Trim(const std::string&) overload.

#include <string>
#include <android-base/strings.h>

namespace android {
namespace base {

std::string Trim(const std::string& s) {
    return Trim(std::string_view(s));
}

}
}
