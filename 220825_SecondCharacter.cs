//https://codelearn.io/training/2358
//Bài này thuật toán của mình 100% nhưng code là chatbot do chưa thông thạo C# vì vậy để hết comment
public char SecondChar(string s)
{
    // 1. Khởi tạo
    // Mảng lưu tần suất của 26 ký tự từ 'a' đến 'z'
    int[] freq = new int[26];

    // Các biến để theo dõi tần suất lớn nhất và lớn thứ nhì
    int maxFreq = 0;
    int secondMaxFreq = 0;

    // Các biến để lưu ký tự tương ứng
    char firstChar = '?';
    char secondChar = '?';

    // 2. Duyệt chuỗi và cập nhật "real-time"
    // Dùng vòng lặp for thay vì foreach
    for (int i = 0; i < s.Length; i++)
    {
        char c = s[i];
        
        // Chuyển ký tự thành chỉ số mảng (0-25) bằng cách trừ đi 97 (mã ASCII của 'a')
        int index = c - 'a';

        // Tăng tần suất của ký tự này lên 1
        freq[index]++;

        // Lấy tần suất hiện tại để so sánh
        int currentFreq = freq[index];

        // 3. Logic so sánh và cập nhật
        if (c == firstChar)
        {
            // Nếu ký tự này vẫn là ký tự nhiều nhất, chỉ cần cập nhật lại tần suất của nó
            maxFreq = currentFreq;
        }
        else if (currentFreq > maxFreq)
        {
            // Tìm thấy một "nhà vua" mới!
            // "Nhà vua" cũ (firstChar) bị giáng xuống làm "á quân" (secondChar)
            secondMaxFreq = maxFreq;
            secondChar = firstChar;
            
            // Cập nhật "nhà vua" mới
            maxFreq = currentFreq;
            firstChar = c;
        }
        else if (currentFreq > secondMaxFreq)
        {
            // Tần suất này không đủ để làm "vua", nhưng đủ để làm "á quân"
            // (Đề bài đảm bảo không có 2 ký tự nào có cùng tần số,
            // nên không cần kiểm tra currentFreq == maxFreq)
            secondMaxFreq = currentFreq;
            secondChar = c;
        }
    }

    // 4. Trả về kết quả
    // Sau khi duyệt xong, secondChar sẽ là ký tự ta cần tìm.
    // Nếu không có ký tự thứ hai, nó sẽ giữ nguyên giá trị khởi tạo là '?'.
    return secondChar;
}
